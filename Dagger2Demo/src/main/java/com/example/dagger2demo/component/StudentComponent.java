package com.example.dagger2demo.component;

import com.example.dagger2demo.MainActivity;

import javax.inject.Singleton;

import dagger.Component;

/**
 * 此处申明一个接口
 * 作用：用于连接  接收类（也就是MainActivity）和被依赖注入类（Student）的连接桥梁
 * 使用 @Component 注解这个接口 Dagger2使用APT会生成一个该接口的实现类DaggerStudentComponent
 * 在该实现类中的injectStudent方法会去调用@Inject修饰的Student构造函数初始化，
 * 并赋值给传入参数也就是MainActivity中被@inject注解的属性，
 * 完成了依赖注入的整个过程
 */
@Singleton
@Component
public interface StudentComponent
{
	void injectStudent(MainActivity activity);
}
