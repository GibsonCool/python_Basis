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
		/**
		 * 前面两步都配置好了后，Student  、StudentComponent
		 * Dagger2是基于APT编译时注解的框架， 需要先build一次，才会生成DaggerStudentComponent类
		 * 然后就可以使用了，可以查看源码框架生成的代码做了什么
		 */
		DaggerStudentComponent.create().injectStudent(this);
		binding.setStudent(student);
	}
}
