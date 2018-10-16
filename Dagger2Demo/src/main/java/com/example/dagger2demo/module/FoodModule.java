package com.example.dagger2demo.module;

import com.example.dagger2demo.javaBean.BaoZi;
import com.example.dagger2demo.javaBean.KangShiFu;

import dagger.Module;
import dagger.Provides;

/**
 * @atuthor cxx
 * @data on 2018/10/16     email:cxxceo@163.com
 * @describe
 */
@Module
public class FoodModule
{
	@Provides
	public BaoZi provideBaoZi(){
		return new BaoZi();
	}

	@Provides
	public KangShiFu provideKangShiFu(){
		return new KangShiFu();
	}
}
