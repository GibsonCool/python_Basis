package com.example.dagger2demo;

import android.app.Activity;
import android.databinding.DataBindingUtil;
import android.os.Bundle;

import com.example.dagger2demo.component.DaggerUserComonent;
import com.example.dagger2demo.databinding.ActivityMain2Binding;
import com.example.dagger2demo.javaBean.User;

import javax.inject.Inject;

public class Main2Activity extends Activity
{

	@Inject
	User user;

	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		ActivityMain2Binding binding = DataBindingUtil.setContentView(this, R.layout.activity_main2);
		DaggerUserComonent.create().injectUser(this);
		binding.setUser(user);
	}
}
