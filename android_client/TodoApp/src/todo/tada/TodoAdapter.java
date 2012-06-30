package todo.tada;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

public class TodoAdapter extends BaseAdapter {

    List<Todo> todos;
    LayoutInflater inflater;

    public TodoAdapter(Context context)
    {
        todos = new ArrayList<Todo>();
        inflater = LayoutInflater.from(context);
    }

    public void addTask(Todo todo)
    {
        todos.add(todo);
        notifyDataSetChanged();
    }

    @Override
    public int getCount()
    {
        return todos.size();
    }

    @Override
    public Todo getItem(int i)
    {
        return todos.get(i);
    }

    @Override
    public long getItemId(int i)
    {
        return i;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup)
    {
        if (view == null)
        {
            view = inflater.inflate(R.layout.todo, null);
        }

        TextView textView = (TextView) view.findViewById(R.id.task);
        textView.setText(todos.get(i).getTask());

        return view;
    }
}
