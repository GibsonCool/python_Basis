package com.example.dagger2demo.component;

import com.example.dagger2demo.SubCompontentActivity;
import com.example.dagger2demo.module.FoodModule;

import dagger.Subcomponent;

/**
 * @atuthor cxx
 * @data on 2018/10/16     email:cxxceo@163.com
 * @describe
 */
@Subcomponent(modules = FoodModule.class)
public interface SubComponent
{
	void inject(SubCompontentActivity activity);
}
