package com.example.kotlinbindingdemo

import android.databinding.DataBindingUtil
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.ViewGroup
import android.widget.Toast
import com.example.kotlinbindingdemo.databinding.ItemRecyclerViewBinding

class MyAdapter(val mDatas: List<User>) : RecyclerView.Adapter<MyAdapter.ViewHolder>() {
    override fun onCreateViewHolder(p0: ViewGroup, p1: Int): ViewHolder {
        val binding: ItemRecyclerViewBinding = DataBindingUtil.inflate(LayoutInflater.from(p0.context), R.layout.item_recycler_view, p0, false)
        return ViewHolder(binding)
    }

    override fun getItemCount(): Int = mDatas.size

    override fun onBindViewHolder(p0: ViewHolder, p1: Int) {
        p0.bind(mDatas[p1])
    }

    class ViewHolder(val binding: ItemRecyclerViewBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(user: User) {
            binding.user = user
            binding.rcPresenter = RcPresenter(binding)
        }
    }

    class RcPresenter(val binding: ItemRecyclerViewBinding) {
        fun onItemClick(user: User): Unit {
            Toast.makeText(binding.root.context, "name: " + user.firstName + "--" + user.lastName + "\tage: " + user.age, Toast.LENGTH_SHORT).show();
        }
    }
}



