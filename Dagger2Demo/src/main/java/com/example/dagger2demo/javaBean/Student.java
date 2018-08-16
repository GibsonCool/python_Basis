package com.example.dagger2demo.javaBean;

import javax.inject.Inject;

public class Student
{
	private String name;
	private int age;

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
