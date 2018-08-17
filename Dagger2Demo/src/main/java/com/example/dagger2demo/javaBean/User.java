package com.example.dagger2demo.javaBean;

/**
 * 假设这个类是第三方框架的类，我们无法直接上使用 @Inject 注解其构造函数
 */
public class User
{
	private String name;

	public User()
	{
		name = "user default name";
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
