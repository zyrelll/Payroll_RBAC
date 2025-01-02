<template>
    <div>
        <h1>Create an account</h1>
        <form>
            <fieldset>
                <label for="username">Username:</label>
                <input 
                    type="text" 
                    name="username"
                    id="username"
                    v-model="registerForm.username"
                    />
                <label for="password">Password:</label>
                <input 
                    type="password"
                    name="password" 
                    id="password"
                    v-model="registerForm.password"
                    />
                <select name="role" id="role" v-model="registerForm.role">
                    <option value="" disabled>Choose role</option>
                    <option value="owner">Owner</option>
                    <option value="finance">Finance Staff</option>
                    <option value="employee">Employee</option>
                </select>
                <button 
                    type="button"
                    @click="handleSubmit"
                    >Submit</button>
            </fieldset>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            registerForm: {
                username: '',
                password: '',
                role: '',
            },
        };
    },
    components: {

    },
    methods: {
        registerUser(payload) {
            const path = `http://localhost:5001/register`;
            axios.post(path, payload)
                .then(() => {
                    console.log("success")
                })
                .catch((error) => {
                    console.error(error)
                });
        },
        // addRule(payload) {
        //     const path = `http://localhost:5001/rules`;
        //     axios.post(path, payload)
        //         .then(() => {
        //             this.getRules();
        //             this.message = 'Rule "' + payload.remark + '" added!'
        //             this.showMessage = !this.showMessage;
        //         })
        //         .catch((error) => {
        //             console.log(error);
        //             this.getRules();
        //         });
        // },
        handleSubmit() {
            const payload = {
                username: this.registerForm.username,
                password: this.registerForm.password,
                role: this.registerForm.role,
            };
            this.registerUser(payload)
            this.initForm();
        },
        initForm() {
            this.registerForm.username = '';
            this.registerForm.password = '';
            this.registerForm.role = '';
        },
    },
};
</script>

<style lang="scss" scoped>

</style>