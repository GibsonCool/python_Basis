package com.example.dagger2demo;

import android.app.Activity;
import android.databinding.DataBindingUtil;
import android.os.Bundle;
import android.util.Log;

import com.example.dagger2demo.annotation.UserParamsWithEmpty;
import com.example.dagger2demo.annotation.UserParamsWithParameter;
import com.example.dagger2demo.component.DaggerUserComonent;
import com.example.dagger2demo.databinding.ActivityMain2Binding;
import com.example.dagger2demo.javaBean.User;
import com.example.dagger2demo.javaBean.UserParams;
import com.example.dagger2demo.module.UserModule;

import javax.inject.Inject;
import javax.inject.Named;

public class Main2Activity extends Activity
{

	@Inject
	User user;

	@Named("params")
	@Inject
	UserParams userParams;

	@Inject
	/**
	 *  @Named 注解虽然可以通过配置不同的注解只让Dagger2去找到对应的方法初始化，但是毕竟是使用的字符串比较也导致在书写的时候出错可能性高
	 *  Dagger2也想到这种问题，查看@Named注解内部实现 内部是通过 @Qualifier注解实现，模仿这个实现自己的注解如：UserParamsWithEmpty、UserParamsWithParameter
	 */
	@Named("empty")
	UserParams userParams2;

	@Inject
	/**
	 * 相对于@Named注解通过注解值字符串配对的方式，两边都需要填写值的方式，这种通过直接写一个针对性的识别限定注解更优雅从代码层面避免人工手写，
	 * 如果不好理解，可以想象成我们switch代码中定义常量使用 1,2,3,4 使用public static final修饰，但是值还是可以用相等的伪装，而使用枚举类直接生成对应类
	 * 就可以避免这种值相等的情况，直接通过类型判断隔离开来。优雅简单且团队开发互相使用也不会出现字符串写错的情况。
	 */
	@UserParamsWithEmpty
	UserParams userParams3;

	@Inject
	@UserParamsWithParameter
	UserParams userParams4;

	private static final String TAG = "Main2Activity";

	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		ActivityMain2Binding binding = DataBindingUtil.setContentView(this, R.layout.activity_main2);
		DaggerUserComonent.builder().userModule(new UserModule("Params user")).build().injectUser(this);
		binding.setUser(user);
		binding.setUserParams(userParams);
		binding.setUserParams2(userParams2);
		binding.setUserParams3(userParams3);
		binding.setUserParams4(userParams4);
		Log.e(TAG, "userParams: " + userParams);
		Log.e(TAG, "userParams name : " + userParams.getName());
		Log.e(TAG, "userParams2: " + userParams2);
		Log.e(TAG, "userParams2 name : " + userParams2.getName());
		Log.e(TAG, "userParams3: " + userParams3);
		Log.e(TAG, "userParams3 name : " + userParams3.getName());
		Log.e(TAG, "userParams4: " + userParams4);
		Log.e(TAG, "userParams4 name : " + userParams4.getName());

	}
}
