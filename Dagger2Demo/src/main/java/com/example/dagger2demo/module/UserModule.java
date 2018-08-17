package com.example.dagger2demo.module;

import com.example.dagger2demo.javaBean.User;

import dagger.Module;
import dagger.Provides;

@Module
public class UserModule
{
	@Provides
	public User provideUser()
	{
		return new User();
	}
}
