package todo.tada;

import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.widget.ListView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.Iterator;

public class MyActivity extends Activity
{
    public TodoAdapter todoAdapter;

    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        ListView todoList = (ListView) findViewById(R.id.todo_list);

        todoAdapter = new TodoAdapter(this);

        todoList.setAdapter(todoAdapter);

        TodoGetterTask task = new TodoGetterTask();

        task.execute("http://169.254.225.196:6767/todo/list");
    }

    class TodoGetterTask extends AsyncTask<String, String, String>
    {
        @Override
        protected String doInBackground(String... strings)
        {
            try
            {
                return new HttpRequestMaker().executeGet(new URI(strings[0]));
            }
            catch (IOException e)
            {
                return null;
            }
            catch (URISyntaxException e)
            {
                return null;
            }
        }

        @Override
        protected void onPostExecute(String result)
        {
            try
            {
                Log.e("MyActivity", "result is " + result);
                JSONArray array = new JSONArray(result);
                for (int i = 0; i < array.length(); i++)
                {
                    JSONObject object = array.getJSONObject(i);
                    Iterator<String> iterator = object.keys();
                    while (iterator.hasNext())
                    {
                        String id = iterator.next();
                        String task = object.getString(id);

                        Todo todo = new Todo(id, task);

                        todoAdapter.addTask(todo);
                    }
                }
            }
            catch (JSONException e)
            {
            }
        }
    }
}
