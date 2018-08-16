package com.example.dagger2demo;

import android.databinding.DataBindingUtil;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.example.dagger2demo.databinding.ActivityMainBinding;
import com.example.dagger2demo.javaBean.Student;

import javax.inject.Inject;

public class MainActivity extends AppCompatActivity
{

	@Inject
	Student student;

	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		ActivityMainBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_main);
		DaggerStudentComponent.create().inject(this);
		binding.setStudent(student);
	}
}
