# Bu kod React funksional komponenti uchun yaratilgan bo'lib, u login formasini email va parol maydonlarini kiritadi.
import React from 'react'

class LoginForm extends React.Component:
    constructor(props):
        super(props)
        this.state = {
            email: '',
            password: ''
        }

    onChangeEmail = (event) => {
        this.setState({ email: event.target.value })
    }

    onChangePassword = (event) => {
        this.setState({ password: event.target.value })
    }

    onSubmit = (event) => {
        event.preventDefault()
        console.log(this.state)
    }

    render() {
        return (
            <div className="max-w-md mx-auto p-8 bg-white rounded-lg shadow-md">
                <h2 className="text-lg font-bold mb-4">Login</h2>
                <form onSubmit={this.onSubmit}>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">Email</label>
                        <input 
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                            id="email" 
                            type="email" 
                            value={this.state.email} 
                            onChange={this.onChangeEmail} 
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">Password</label>
                        <input 
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                            id="password" 
                            type="password" 
                            value={this.state.password} 
                            onChange={this.onChangePassword} 
                        />
                    </div>
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">Login</button>
                </form>
            </div>
        )
    }
```

Bu kod React funksional komponenti uchun yaratilgan bo'lib, u login formasini email va parol maydonlarini kiritadi. Komponentda email va parol maydonlari mavjud bo'lib, ularni kiritish uchun input elementlari ishlatiladi. Login tugmasi bosilganda, komponentda `onSubmit` metodi ishlaydi va login ma'lumotlarini konsolga chiqaradi.
