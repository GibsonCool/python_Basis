package com.example.bindingdemo;

import android.app.Activity;
import android.databinding.DataBindingUtil;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.widget.LinearLayoutManager;
import android.view.View;
import android.widget.Toast;

import com.example.bindingdemo.adapter.UserObAdatper;
import com.example.bindingdemo.bean.UserOB;
import com.example.bindingdemo.databinding.ActivityRecycleviewBinding;

import java.util.ArrayList;
import java.util.List;

public class RecyclerViewActivity extends Activity
{
	ActivityRecycleviewBinding binding;
	UserObAdatper adatper;
	@Override
	protected void onCreate(@Nullable Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		binding = DataBindingUtil.setContentView(this, R.layout.activity_recycleview);
		binding.setPresenter(new Presenter());
		binding.recycleView.setLayoutManager(new LinearLayoutManager(this));
		adatper = new UserObAdatper(this);
		binding.recycleView.setAdapter(adatper);
		adatper.setmListener(new UserObAdatper.OnItemClickListener()
		{
			@Override
			public void onUserObClick(UserOB userOB)
			{
				Toast.makeText(RecyclerViewActivity.this,userOB.getFirstName(),Toast.LENGTH_SHORT).show();
			}
		});
		List<UserOB> testList = new ArrayList<>();
		testList.add(new UserOB("cxx","666"));
		testList.add(new UserOB("cxx2","6466",true));
		testList.add(new UserOB("cxx3","6====66",true));
		testList.add(new UserOB("gibson","cool"));
		adatper.addAll(testList);

	}

	public class Presenter
	{
		public void onClickAddItem(View view)
		{
			Toast.makeText(view.getContext(),"增加",Toast.LENGTH_SHORT).show();
			adatper.add(new UserOB("增加","dadada",true));
		}

		public void onClickRemoveItem(View view)
		{
			Toast.makeText(view.getContext(),"减少",Toast.LENGTH_SHORT).show();
			adatper.remove();
		}
	}
}
