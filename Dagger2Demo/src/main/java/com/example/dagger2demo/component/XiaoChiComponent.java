package com.example.dagger2demo.component;

import com.example.dagger2demo.javaBean.GuaZi;
import com.example.dagger2demo.javaBean.HuoTuiChang;
import com.example.dagger2demo.module.XiaoChiModule;

import dagger.Component;

/**
 * @atuthor cxx
 * @data on 2018/10/16     email:cxxceo@163.com
 * @describe
 */
@Component(modules = XiaoChiModule.class)
public interface XiaoChiComponent
{
	GuaZi provideGuaZi();

	HuoTuiChang provideHuoTuiChang();
}
