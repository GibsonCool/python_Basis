package com.example.kotlindatabindingsample

import android.app.Activity
import android.databinding.DataBindingUtil
import android.os.Bundle
import android.view.View
import android.widget.Toast
import com.example.kotlindatabindingsample.databinding.ActivitySimpleBinding

class SimpleActivity : Activity() {

    val user = User("Gibson", "cool")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding = DataBindingUtil.setContentView<ActivitySimpleBinding>(this, R.layout.activity_simple)
        user.map.put("A","AAA")
        user.map.put("B","BBB")
        user.map.put("C","CCC")
        binding.user = user
        binding.presenter = Presenter()
        binding.viewStub.viewStub?.inflate()
    }

    inner class Presenter {

        fun onTextChanged(s: CharSequence, start: Int, before: Int, count: Int) {
            user.firstName.set(s.toString())
            user.isFired.set(!user.isFired.get())
        }

        fun onClick(view: View) = Toast.makeText(this@SimpleActivity, "点击了", Toast.LENGTH_SHORT).show()

        fun onClickListenerBinding(user: User) = Toast.makeText(this@SimpleActivity, user.lastName.get(), Toast.LENGTH_SHORT).show()

    }
}
