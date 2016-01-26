package finalProject;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map.Entry;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.NumericRangeQuery;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;

public class GetAverageRating2014 {

	private static void updateRatings(String id,
			HashMap<String, Float> ratings, String rating) {
		String[] rating_count = rating.split("  ");
		//System.out.println(rating_count.length);
		//for(int i = 0; i < rating_count.length; i++){
			//System.out.println(rating_count[i]);
		//}
		int totalrate = Integer.parseInt(rating_count[1].trim())
				+ Integer.parseInt(rating_count[2].trim())
				+ Integer.parseInt(rating_count[3].trim())
				+ Integer.parseInt(rating_count[4].trim())
				+ Integer.parseInt(rating_count[5].trim());
		
		//System.out.println("total " + totalrate);
		float newrate = 0;
		if(totalrate != 0){
		newrate = (Integer.parseInt(rating_count[1].trim()) * 1
				+ Integer.parseInt(rating_count[2].trim()) * 2
				+ Integer.parseInt(rating_count[3].trim()) * 3
				+ Integer.parseInt(rating_count[4].trim()) * 4
				+ Integer.parseInt(rating_count[5].trim()) * 5)/totalrate;
		
		if(newrate > 0){
			if(ratings.get(id)== null){
				ratings.put(id, newrate);
			}else{
				ratings.put(id, (ratings.get(id) + newrate)/2);
			}
		}
		}
	}

	private static void fileReviews(String filename, String year,
			HashMap<String, Float> ratings) {

		PrintWriter writer = null;

		
			try {
				writer = new PrintWriter(new FileOutputStream(new File(
						"C:\\Users\\ShravanJagadish\\Desktop\\Search\\Final Project\\Output\\Ground Truth\\"
								+ year + "\\" + filename 
								+ ".txt"), true));
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			for (Entry<String, Float> entry : ratings.entrySet()) {
			writer.append(entry.getKey() + "::" + (entry.getValue()).toString() + "\n");					
		}
		writer.close();

	}

	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		try {
			IndexReader reader = DirectoryReader
					.open(FSDirectory.open(Paths
							.get("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Index")));
			IndexSearcher searcher = new IndexSearcher(reader);
			/**
			 * Get query terms from the query string
			 */

			Query querys = NumericRangeQuery.newIntRange("DATE", 20140101,
					20141231, true, true);

			HashMap<String, Float> ratings = new HashMap<String, Float>();

			TopDocs docs = searcher.search(querys, 1);
			// System.out.println(docs.totalHits);
			TopDocs topDoc = searcher.search(querys, docs.totalHits);

			for (ScoreDoc scoreDoc : topDoc.scoreDocs) {
				Document doc = searcher.doc(scoreDoc.doc);
				String id = doc.get("BID");
				id = id.replaceAll(" ", "");
				//String date = doc.get("DATE");
				String rating = doc.get("RATING");
				//System.out.println(id + " " + rating);
				updateRatings(id, ratings, rating);

			}
			
			//for (Entry<String, Float> entry : ratings.entrySet()) {
			//	System.out.println(entry.getKey() + " : " + entry.getValue());
			//}
			
			fileReviews("GroundTruth_Bakeries", "14", ratings);
			// fileReviewsUnseperated("Bakeries", "14", posReviews, negReviews);
		} catch (Exception e) {
			System.out.println(e);
		}
	}

}
