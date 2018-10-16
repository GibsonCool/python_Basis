package com.example.dagger2demo.module;

import com.example.dagger2demo.annotation.UserParamsWithEmpty;
import com.example.dagger2demo.annotation.UserParamsWithForce;
import com.example.dagger2demo.annotation.UserParamsWithLazy;
import com.example.dagger2demo.annotation.UserParamsWithParameter;
import com.example.dagger2demo.javaBean.User;
import com.example.dagger2demo.javaBean.UserParams;

import javax.inject.Named;

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

	private String name;

	/**
	 * 如果一个 Module 没有实现任何构造方法，那么在 Component 中 Dagger2 会自动创建，如果这个 Module 实现了有参的构造方法，那么它需要在 Component 构建的时候手动传递进去
	 * @param name
	 */
	public UserModule(String name)
	{
		this.name = name;
	}

	@Provides
	public String provideName()
	{
		return name;
	}


	/**
	 * 返回一个带参数构造函数的依赖注入对象 ，如果Main2Activity中有多个UserParams字段，可以使用Singleton注解
	 * 其内部在生成的代码中会有DoubleCheck在生成的时候去双重检锁保持单列
	 *
	 * @param name
	 * @return
	 */
	@Named("params")        //用于不同需求调用有参构造方法创建对象
	@Provides
	public UserParams provideUserParams(String name)
	{
		return new UserParams(name);
	}

	/**
	 * 用于调用UserParams的无参构造函数生成对象
	 *
	 * @return
	 */
	@Named("empty")        //用于不同需求依赖注入字段需要使用无参构造函数创建对象,
	@Provides
	public UserParams provideUserParamsNone()
	{
		return new UserParams();
	}

	@UserParamsWithParameter
	@Provides
	public UserParams provideUserParamsAnotation()
	{
		return new UserParams("created by provideUserParamsAnotation");
	}

	@UserParamsWithEmpty
	@Provides
	public UserParams provideUserParamsAnotationEmpty()
	{
		return new UserParams(" created by provideUserParamsAnotationEmpty");
	}

	@UserParamsWithLazy
	@Provides
	public UserParams provideUserParamsAnotationLazy()
	{
		return new UserParams(" created by UserParamsWithLazy");
	}

	@UserParamsWithForce
	@Provides
	public UserParams provideUserParamsAnotationForce()
	{
		return new UserParams(" created by 强制加载");
	}
}
