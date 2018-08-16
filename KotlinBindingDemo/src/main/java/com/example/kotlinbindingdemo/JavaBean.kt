package com.example.kotlinbindingdemo

import android.databinding.ObservableField

data class User(var firstName: String, var lastName: String, var age: Int)

data class UserObservable(var name: ObservableField<String>, var url: ObservableField<String>)