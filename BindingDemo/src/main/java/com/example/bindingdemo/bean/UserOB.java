package com.example.bindingdemo.bean;

import android.databinding.BaseObservable;
import android.databinding.Bindable;
import android.databinding.ObservableBoolean;

import com.example.bindingdemo.BR;

public class UserOB extends BaseObservable
{
	private String firstName;
	private String lastName;
	public ObservableBoolean isVisible = new ObservableBoolean();

	public UserOB(String firstName, String lastName)
	{
		this.firstName = firstName;
		this.lastName = lastName;
		this.isVisible.set(false);
	}

	public UserOB(String firstName, String lastName, boolean isVisible)
	{
		this.firstName = firstName;
		this.lastName = lastName;
		this.isVisible.set(isVisible);
	}

	@Bindable
	public String getFirstName()
	{
		return firstName;
	}

	@Bindable
	public String getLastName()
	{
		return lastName;
	}

	public void setFirstName(String firstName)
	{
		this.firstName = firstName;
		notifyPropertyChanged(BR.firstName);    //只刷新这个字段
	}

	public void setLastName(String lastName)
	{
		this.lastName = lastName;
		notifyChange();    //刷新所有
	}

	public boolean getIsVisible()
	{
		return isVisible.get();
	}

	public void setIsVisible(boolean isVisible)
	{
		this.isVisible.set(isVisible);
	}
}
