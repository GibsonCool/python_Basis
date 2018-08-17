package com.example.dagger2demo;

import javax.inject.Singleton;

import dagger.Component;

/**
 * 此处申明一个接口
 * 作用：用于连接  接收类（也就是MainActivity）和被依赖注入类（Student）的连接桥梁
 * 使用 @Component 注解这个接口 Dagger2使用APT会生成一个该接口的实现类DaggerStudentComponent
 * 并且包含一个方法用于将需要使用到依赖注入的类（接收类）对象传递进来例如这里是MainActivity
 */
@Singleton
@Component
public interface StudentComponent
{
	void injectStudent(MainActivity activity);
}
