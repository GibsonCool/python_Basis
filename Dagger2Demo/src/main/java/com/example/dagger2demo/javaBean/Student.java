package com.example.dagger2demo.javaBean;

import javax.inject.Inject;


public class Student
{
	private String name;
	private int    age;

	/**
	 * 需要被注入的类，构造方法用@Inject关键字修饰
	 * Dagger2 框架在为我们初始化的时候回调用这个构造函数
	 */
	@Inject
	public Student()
	{
		this.name = "GibsonCool";
		this.age = 24;
	}


	public String getName()
	{
		return name;
	}

	public void setName(String name)
	{
		this.name = name;
	}

	public int getAge()
	{
		return age;
	}

	public void setAge(int age)
	{
		this.age = age;
	}
}
