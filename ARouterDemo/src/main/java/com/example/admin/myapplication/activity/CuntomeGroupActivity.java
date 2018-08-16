package com.example.admin.myapplication.activity;

import android.app.Activity;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.widget.TextView;

import com.alibaba.android.arouter.facade.annotation.Route;
import com.example.admin.myapplication.R;

@Route(path = "/com/CustomeGroupActivity", group = "constomeGroup")
public class CuntomeGroupActivity extends Activity
{
	@Override
	protected void onCreate(@Nullable Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_first);
		String name = getIntent().getStringExtra("name");

		TextView tv = findViewById(R.id.text);
		tv.setText(name);
	}
}
