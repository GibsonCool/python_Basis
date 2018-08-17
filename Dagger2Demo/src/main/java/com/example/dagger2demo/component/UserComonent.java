package com.example.dagger2demo.component;

import com.example.dagger2demo.Main2Activity;
import com.example.dagger2demo.module.UserModule;

import javax.inject.Singleton;

import dagger.Component;

/**
 * 与使用@Inject一样的，此处也需要提供一个Component(DaggerUserComonent)来连接接受者Main2Activity和需要依赖注入的User
 * DaggerUserComonent实现类中初始化的时候会去初始化@Component注解之中的modules对应class的对象(这里就是UserModule实例)，
 * 在调用injectUser的时候则会去调用UserModule中@Provides的方法返回与接受者Main2Activity中@Inject注解的字段对应的类型并赋值
 * 完成依赖注入
 */
@Singleton        //因为UserModule中UserParams需要单例使用了@Singleton注解这里也需要
@Component(modules = {UserModule.class})
public interface UserComonent
{
	void injectUser(Main2Activity activity);
}
