package com.example.dagger2demo;

import javax.inject.Singleton;

import dagger.Component;

@Singleton
@Component
public interface StudentComponent
{
	void inject(MainActivity activity);
}
