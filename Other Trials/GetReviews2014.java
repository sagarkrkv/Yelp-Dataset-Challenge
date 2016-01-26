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

public class GetReviews2014 {

	private static HashMap<Integer, String> months = new HashMap<Integer, String>();

	private static void loadMonths() {
		months.put(1, "Jan");
		months.put(2, "Feb");
		months.put(3, "Mar");
		months.put(4, "Apr");
		months.put(5, "May");
		months.put(6, "Jun");
		months.put(7, "Jul");
		months.put(8, "Aug");
		months.put(9, "Sep");
		months.put(10, "Oct");
		months.put(11, "Nov");
		months.put(12, "Dec");
	}

	private static String[] getMonthAndYear(String date) {
		String output[] = new String[2];
		output[0] = months.get(Integer.parseInt(date.substring(4, 6)));
		output[1] = date.substring(0, 4);
		// System.out.println(output[0] + " " + output[1]);
		return output;
	}

	private static void updateReviews(String neg, String pos, String id,
			HashMap<String, String> posReviews,
			HashMap<String, String> negReviews) {
		negReviews.put(id, negReviews.get(id) + neg);
		posReviews.put(id, posReviews.get(id) + pos);
	}

	private static void fileReviews(String filename, String year,
			HashMap<String, String> posReviews,
			HashMap<String, String> negReviews) {
		
		PrintWriter writer = null;
		
		
		
		for (Entry<String, String> entry : posReviews.entrySet()) {
			try {
				writer = new PrintWriter(new FileOutputStream(new File(
						"C:\\Users\\ShravanJagadish\\Desktop\\Search\\Final Project\\Output\\"
								+ year + "\\"  + entry.getKey() +"_"
								+ filename + ".txt"), true));
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}			
			writer.append(entry.getValue());
			writer.append(negReviews.get(entry.getKey()));
			writer.close();
		}
		
		


	}
	
	
	private static void fileReviewsUnseperated(String filename, String year,
			HashMap<String, String> posReviews,
			HashMap<String, String> negReviews) {
		
		PrintWriter writer = null;
		try {
			writer = new PrintWriter(new FileOutputStream(new File(
					"C:\\Users\\ShravanJagadish\\Desktop\\Search\\Final Project\\Output\\"
							+ year + "\\"
							+ filename + ".txt"), true));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		for (Entry<String, String> entry : posReviews.entrySet()) {
			writer.append(entry.getValue());			
		}
		for (Entry<String, String> entry : negReviews.entrySet()) {
			writer.append(entry.getValue());			
		}
			
		writer.close();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		loadMonths();
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

			HashMap<String, String> posReviews = new HashMap<String, String>();
			HashMap<String, String> negReviews = new HashMap<String, String>();

			TopDocs docs = searcher.search(querys, 1);
			// System.out.println(docs.totalHits);
			TopDocs topDoc = searcher.search(querys, docs.totalHits);

			for (ScoreDoc scoreDoc : topDoc.scoreDocs) {
				Document doc = searcher.doc(scoreDoc.doc);
				String id = doc.get("BID");
				id = id.replaceAll(" ", "");
				
				String neg = doc.get("REV_TEXT1") + " " + doc.get("REV_TEXT2")
						+ " " + doc.get("REV_TEXT3");
				String pos = doc.get("REV_TEXT4") + " " + doc.get("REV_TEXT5");
				String date = doc.get("DATE");
				//String[] monyr = getMonthAndYear(date);

				// System.out.println("Month :: " + monyr[0] +
				// " Year :: " +
				// monyr[1]);

				updateReviews(neg, pos, id, posReviews, negReviews);

			}

			fileReviews("Bakeries", "14", posReviews, negReviews);
			//fileReviewsUnseperated("Bakeries", "14", posReviews, negReviews);
		} catch (Exception e) {
			System.out.println(e);
		}
	}

}
