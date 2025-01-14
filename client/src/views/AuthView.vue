<template>
<div class='grid grid-cols-12'>
        <div class="col-span-4 text-white font-sans font-bold bg-black min-h-screen pl-7">
            <div class="grid grid-rows-6 grid-flow-col min-h-screen items-center justify-items-start">
                <div class="row-span-4 row-start-2 text-4xl">
                    PT. XYZ
                    <p class="text-2xl">Payroll Managament System</p>
                    <form>
                        <div class="pt-10 pr-20">                        
                            <label class="text-sm font-sans font-medium">
                                Username
                            </label>
                            <input 
                                type="text" 
                                name="username" 
                                v-model="loginForm.username"
                                placeholder="ex: U554424" 
                                class="w-full bg-black py-3 px-12 border hover: border-gray-500 rounded shadow text-base font-sans"/>                            
                        </div>
                        <div class="pt-2 pr-20">
                            <label class="text-sm font-sans font-medium">
                                Password
                            </label>
                            <input 
                                type="password" 
                                name="password"  
                                v-model="loginForm.password"
                                class=" w-full bg-black py-3 px-12 border hover: border-gray-500 rounded shadow text-base font-sans"/>
                        </div>
                        <!-- Button -->
                        <div class="text-sm font-sans font-medium w-full pr-20 pt-14">
                            <button 
                                type="button"   
                                @click="handleSubmit"
                                class="text-center w-full py-4 bg-blue-700 hover:bg-blue-400 rounded-md text-white">
                                    LOG IN
                            </button>
                        </div>
                   </form>
                </div>
            </div>         
        </div>
        <div class="banner col-span-8 bg-black">
            <img src="../assets/img/bg_login.jpg" alt="Login Background Image">
        </div>
    </div>  
</template>

<style>
    img {
        background-repeat: repeat;  
        /* background-size: cover; */
    }
</style>

<script>
import axios from 'axios';
const instance = axios.create({
    baseURL: 'http://localhost:5001', //alamat backend
    withCredentials: true, //include cookies
});

// Add CSRF token to every request
instance.interceptors.request.use(config => {
    const csrfToken = document.cookie.split('; ').find(row =>
    row.startsWith('csrf_access_token='))?.split('=')[1];
    if (csrfToken) {
        config.headers['X-CSRF-TOKEN'] = csrfToken;
    }
    return config;
}) // INI DIPAKE COK
export default {
    data() {
        return {
            loginForm: {     
                username: '',
                password: '',
            },
            users: [],
        };
    },
    components: {

    },
    methods: {
        roleRedirect(payload) {
            const path = 'http://localhost:5001/getRole';
            axios.get(path, payload, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': this.$cookies.get('access-token'),
                    }
                })
                .then(response => {
                    // this.$router.push('/')
                })
                .catch(error => {
                    console.error('Error:', error);
                })
        },
        async login(payload) {
            try {
                const path = 'http://localhost:5001/login';
                const response = await axios.post(path, payload, {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    withCredentials: true, // This should be outside the headers
                });
                console.log('Login successful: ', response.data);
            } catch (error) {
                console.error('Error logging in:', error.response?.data || error.message);
            }
        },
        async getRole() {
            try {
                const path = 'http://localhost:5001/role';
                const response = await axios.get(path, {
                    withCredentials: true, // This should be outside the headers
                });
                console.log('Role: ', response.data);
                $cookies.set('Role', response.data);
                this.$router.push('/');
            } catch (error) {
                console.error('Error fetching user role:', error.response?.data || error.message );
            }
        },
        async handleSubmit() {
            const payload = {
                username: this.loginForm.username,
                password: this.loginForm.password,
            };
            await this.login(payload);
            await this.getRole();
            this.initForm();
        },
        initForm() {
            this.loginForm.username = '';
            this.loginForm.password = '';
        },
    },
};
</script>