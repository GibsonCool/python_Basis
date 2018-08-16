package com.example.admin.myapplication.activity;

import android.app.Activity;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.webkit.WebView;

import com.alibaba.android.arouter.facade.annotation.Route;
import com.example.admin.myapplication.R;

@Route(path = "/com/urlReceiver")
public class URLReceiveActivity extends Activity
{
	@Override
	protected void onCreate(@Nullable Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_url_receive);
		WebView webView = findViewById(R.id.webview);
		webView.loadUrl("file:///android_asset/urltest.html");
	}
}
