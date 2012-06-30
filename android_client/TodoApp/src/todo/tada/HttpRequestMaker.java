package todo.tada;

import android.util.Log;
import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.StatusLine;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.net.URI;

public class HttpRequestMaker
{
    HttpClient client;

    public HttpRequestMaker()
    {
        client = new DefaultHttpClient();
    }

    public String executeGet(URI url) throws IOException
    {
        Log.e("HTTPRequestMaker", "Starting get");

        HttpResponse response = null;
        try
        {
            response = client.execute(new HttpGet(url));
        }
        catch (Exception e)
        {
            Log.e("HTTPRequestMaker", e.getMessage() + " ");
            e.printStackTrace();
        }

        Log.e("HTTPRequestMaker", "execution complete");

        StatusLine statusLine = response.getStatusLine();
        if(statusLine.getStatusCode() == HttpStatus.SC_OK){
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            response.getEntity().writeTo(out);
            out.close();
            String responseString = out.toString();
            return responseString;
        }
        else
        {
            response.getEntity().getContent().close();
            throw new IOException(statusLine.getReasonPhrase());
        }
    }

    public String executePost(URI url, String payload) throws IOException
    {
        Log.e("HTTPRequestMaker", "Starting post");

        HttpResponse response = null;
        try
        {
            response = client.execute(new HttpGet(url));
        }
        catch (Exception e)
        {
            Log.e("HTTPRequestMaker", e.getMessage());
        }

        Log.e("HTTPRequestMaker", "execution complete");

        StatusLine statusLine = response.getStatusLine();
        if(statusLine.getStatusCode() == HttpStatus.SC_OK){
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            response.getEntity().writeTo(out);
            out.close();
            String responseString = out.toString();
            return responseString;
        }
        else
        {
            response.getEntity().getContent().close();
            throw new IOException(statusLine.getReasonPhrase());
        }
    }
}
