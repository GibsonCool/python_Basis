package com.example.bindingdemo.adapter;

import android.content.Context;
import android.databinding.DataBindingUtil;
import android.databinding.ViewDataBinding;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.example.bindingdemo.BR;
import com.example.bindingdemo.R;
import com.example.bindingdemo.bean.UserOB;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class UserObAdatper extends RecyclerView.Adapter<BindingViewHolder>
{
	private static final int NO  = 1;
	private static final int OFF = 2;

	private final LayoutInflater mLayoutInfolater;

	public void setmListener(OnItemClickListener mListener)
	{
		this.mListener = mListener;
	}

	private OnItemClickListener mListener;
	private List<UserOB>        mDatas;

	public interface OnItemClickListener
	{
		void onUserObClick(UserOB userOB);
	}

	public UserObAdatper(Context context)
	{
		mLayoutInfolater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
		mDatas = new ArrayList<>();
	}

	@Override
	public BindingViewHolder onCreateViewHolder(ViewGroup parent, int viewType)
	{
		ViewDataBinding binding;
		if (viewType == NO)
		{
			binding = DataBindingUtil.inflate(mLayoutInfolater, R.layout.item_userob_no, parent, false);
		}
		else
		{
			binding = DataBindingUtil.inflate(mLayoutInfolater, R.layout.item_userob_off, parent, false);
		}
		return new BindingViewHolder(binding);
	}

	@Override
	public void onBindViewHolder(BindingViewHolder holder, int position)
	{
		final UserOB userOB = mDatas.get(position);
		holder.getBinding().setVariable(BR.item, userOB);
		holder.getBinding().executePendingBindings();    //即时刷新数据
		holder.itemView.setOnClickListener(new View.OnClickListener()
		{
			@Override
			public void onClick(View v)
			{
				if (mListener != null)
				{
					mListener.onUserObClick(userOB);
				}
			}
		});
	}

	@Override
	public int getItemCount()
	{
		return mDatas.size();
	}

	@Override
	public int getItemViewType(int position)
	{
		return mDatas.get(position).getIsVisible() ?  OFF : NO;
	}

	public void addAll(List<UserOB> list)
	{
		mDatas.addAll(list);
	}

	Random random = new Random(System.currentTimeMillis());

	public void add(UserOB userOB)
	{
		int index = random.nextInt(mDatas.size() + 1);
		mDatas.add(index, userOB);
		notifyItemInserted(index);
	}

	public void remove()
	{
		if (mDatas.size() == 0) return;
		int index = random.nextInt(mDatas.size());
		mDatas.remove(index);
		notifyItemRemoved(index);
	}
}
