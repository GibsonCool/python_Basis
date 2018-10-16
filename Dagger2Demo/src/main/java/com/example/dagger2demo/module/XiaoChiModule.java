package com.example.dagger2demo.module;

import com.example.dagger2demo.javaBean.GuaZi;
import com.example.dagger2demo.javaBean.HuoTuiChang;

import dagger.Module;
import dagger.Provides;

/**
 * @atuthor cxx
 * @data on 2018/10/16     email:cxxceo@163.com
 * @describe
 */
@Module
public class XiaoChiModule
{
	@Provides
	public GuaZi provideGuazi(){
		return new GuaZi();
	}

	@Provides
	public HuoTuiChang provideHuoTuiChang(){
		return new HuoTuiChang();
	}
}
