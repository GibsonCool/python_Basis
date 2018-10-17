package com.example.dagger2demo;

import android.databinding.DataBindingUtil;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;

import com.example.dagger2demo.component.DaggerParentComponent;
import com.example.dagger2demo.databinding.ActivityComponentDependenciesBinding;
import com.example.dagger2demo.javaBean.BaoZi;
import com.example.dagger2demo.javaBean.GuaZi;
import com.example.dagger2demo.javaBean.HuoTuiChang;
import com.example.dagger2demo.javaBean.KangShiFu;

import javax.inject.Inject;

public class SubCompontentActivity extends AppCompatActivity
{

	@Inject
	HuoTuiChang huoTuiChang;
	@Inject
	GuaZi guaZi;
	@Inject
	BaoZi baozi;
	@Inject
	KangShiFu kangShiFu;

	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		ActivityComponentDependenciesBinding binding = DataBindingUtil.setContentView(this,R.layout.activity_component_dependencies);
		DaggerParentComponent.builder().build().provideSubComponent().inject(this);

		setTitle("SubCompontentActivity");

		binding.setBaozi(baozi);
		binding.setGuazi(guaZi);
		binding.setHuotuichang(huoTuiChang);
		binding.setKangshifu(kangShiFu);

	}


}
