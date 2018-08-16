package com.example.bindingdemo;

import android.content.Intent;
import android.databinding.DataBindingUtil;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import com.example.bindingdemo.bean.User;
import com.example.bindingdemo.bean.UserOB;
import com.example.bindingdemo.databinding.ActivityMainBinding;

import java.util.HashMap;

public class MainActivity extends AppCompatActivity
{
	User   user = new User("xinxing", "chen");
	UserOB userOb = new UserOB("gibson", "cool");
	ActivityMainBinding binding;
	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		binding = DataBindingUtil.setContentView(this, R.layout.activity_main);
		binding.setUser(user);
		binding.setUserOb(userOb);
		/**
		 * 使用了setUser(user)之后  在直接调用设置内容以下代码不生效
		 * 	binding.firstName.setText("gibson");
		 *  binding.lastName.setText(user.getFirstName());
		 */
		HashMap<String,String> map = new HashMap<>();
		map.put("key","key-value");
		map.put("key2","vvvvv");
		binding.setMaps(map);
		binding.setHandler(new Myhandlers());

	}


	public class Myhandlers
	{
		public void onClick(View view)
		{
//			Toast.makeText(view.getContext(),"被点击了",Toast.LENGTH_SHORT).show();
			user.setFirstName("gison");
			binding.setUser(user);
		}
		public void onClickOb(View view)
		{
			/**
			 * UserOb 继承了 BaseObservable 可以不用再低调用 binding.setUserOb() 数据就可以刷新
			 */
			userOb.setLastName("observer change");
		}

		public void onTextChanged(CharSequence text, int start, int lengthBefore, int lengthAfter)
		{
			user.setFirstName(text.toString());
			binding.setUser(user);
		}

		public void changeLasterName(String text){
			user.setLastName(text+"sss");
			binding.setUser(user);
		}

		public void onClickRecyclerView(View view){
			Intent intent = new Intent();
			intent.setClass(MainActivity.this,RecyclerViewActivity.class);
			startActivity(intent );
		}

		public void jumpToOtherActivity(String name){
			Log.e("cxx",name);
			Intent intent = new Intent();
//			intent.setClass(MainActivity.this,ViewSubAndIncludeActivity.class);
			startActivity(intent );
		}
	}
}
