package com.example.admin.myapplication;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;

import com.alibaba.android.arouter.facade.Postcard;
import com.alibaba.android.arouter.facade.callback.NavCallback;
import com.alibaba.android.arouter.facade.callback.NavigationCallback;
import com.alibaba.android.arouter.launcher.ARouter;

public class MainActivity extends AppCompatActivity implements View.OnClickListener
{
	public static final String TAG = "ARouter";
	FragmentManager fragmentManager;
	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		fragmentManager = getSupportFragmentManager();

		/**
		 * 最简单的跳转
		 */
		findViewById(R.id.bt_frist).setOnClickListener(this);

		/**
		 * 带回调监听的跳转
		 */
		findViewById(R.id.bt_two).setOnClickListener(this);

		/**
		 * 带参数传递的调换
		 */
		findViewById(R.id.bt_three).setOnClickListener(this);

		/**
		 * 带参数传递的调换
		 */
		findViewById(R.id.bt_four).setOnClickListener(this);

		/**
		 * fragment
		 */
		findViewById(R.id.bt_five).setOnClickListener(this);
		/**
		 * 创建URL 中间跳转页
		 */
		findViewById(R.id.bt_url_receive).setOnClickListener(this);
	}

	@Override
	public void onClick(View v)
	{
		switch (v.getId())
		{
			case R.id.bt_frist:
//				ARouter.getInstance().build("/testtest/activity").navigation();
				ARouter.getInstance().build("/test/activity").navigation();
				break;
			case R.id.bt_two:
				ARouter.getInstance()
						.build("/test/activity")
						.navigation(getApplication(), new NavigationCallback()
						{
							@Override
							public void onFound(Postcard postcard)
							{
								Log.e(TAG, "onFound--->找到了");
								Log.e(TAG, "group:" + postcard.getGroup() + "  action:" + postcard.getAction() +
										" name:" + postcard.getName() + " path:" + postcard.getPath());
							}

							@Override
							public void onLost(Postcard postcard)
							{
								Log.e(TAG, "onLost--->找不到目标");

							}

							@Override
							public void onArrival(Postcard postcard)
							{

								Log.e(TAG, "onArrival--->跳转完毕");
							}

							@Override
							public void onInterrupt(Postcard postcard)
							{

								Log.e(TAG, "onInterrupt--->被拦截了");
							}
						});
				break;
			case R.id.bt_three:
				ARouter.getInstance()
						.build("/test/activity")
						.withString("name", "gibsoncool")
						.navigation();
				break;
			case R.id.bt_four:
				ARouter.getInstance()
						.build("/com/CustomeGroupActivity", "constomeGroup")
						.withString("name", "come from custome ")
						.navigation(getApplication(), new NavCallback()
						{
							@Override
							public void onArrival(Postcard postcard)
							{
								Log.e(TAG, "group:" + postcard.getGroup() + "  action:" + postcard.getAction() +
										" name:" + postcard.getName() + " path:" + postcard.getPath());
							}
						});
				break;
			case R.id.bt_five:
				Fragment fragment = (Fragment) ARouter.getInstance()
						.build("/com/testfragment")
						.navigation();
				Log.e(TAG,"start");
				FragmentTransaction transaction = fragmentManager.beginTransaction().add(R.id.fragment_layout, fragment);
				transaction.commit();
				Log.e(TAG,"end");

				break;

			case R.id.bt_url_receive:
				ARouter.getInstance().build("com/urlReceiver").navigation();
				break;
		}
	}
}
