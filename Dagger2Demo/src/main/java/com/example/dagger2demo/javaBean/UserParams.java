package com.example.dagger2demo.javaBean;

/**
 * 带有参数的依赖对象
 */
public class UserParams
{
	private String name;

	public UserParams()
	{
		this.name = "哈哈无参构造函数创建";
	}

	public UserParams(String name)
	{
		this.name = name;
	}

	public String getName()
	{
		return name;
	}

	public void setName(String name)
	{
		this.name = name;
	}


}
