package com.example.bindingdemo.adapter;

import android.databinding.ViewDataBinding;
import android.support.v7.widget.RecyclerView;

public class BindingViewHolder<T extends ViewDataBinding> extends RecyclerView.ViewHolder
{
	protected final T binding;

	public BindingViewHolder(T binding)
	{
		super(binding.getRoot());
		this.binding = binding;
	}

	public T getBinding()
	{
		return binding;
	}
}
