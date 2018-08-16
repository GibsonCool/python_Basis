package com.example.admin.myapplication;

import android.app.Application;

import com.alibaba.android.arouter.launcher.ARouter;

public class App extends Application
{
	@Override
	public void onCreate()
	{
		super.onCreate();
		ARouter.openLog();     // 打印日志
		ARouter.openDebug();
		ARouter.init(this);
	}
}
