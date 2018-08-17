package com.example.dagger2demo.module;

import com.example.dagger2demo.javaBean.User;

import dagger.Module;
import dagger.Provides;

/**
 *
 */
@Module
public class UserModule
{

	/**
	 * @return
	 * @Provides 注解后Dagger2在实例化User类的时候会调用UserModule对象的该方法
	 */
	@Provides
	public User provideUser()
	{
		return new User();
	}
}
