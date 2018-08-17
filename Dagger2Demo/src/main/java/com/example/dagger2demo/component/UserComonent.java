package com.example.dagger2demo.component;

import com.example.dagger2demo.Main2Activity;
import com.example.dagger2demo.module.UserModule;

import dagger.Component;

@Component(modules = {UserModule.class})
public interface UserComonent
{
	void injectUser(Main2Activity activity);
}
