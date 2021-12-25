<template>
    <div class="signup">
        <div class="hero is-primary">
            <div class="hero-body has-text-centered">
                <p class="title">Sign Up</p>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-4 is-offset-4">
                        <form v-on:submit.prevent="onSubmit">
                            <div class="field">
                                <label for="username" class="label">Username</label>
                                <div class="control has-icons-left">
                                    <input type="text" name="username" id="" class="input">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-user"></i>
                                    </span>
                                </div>
                            </div>

                            <div class="field">
                                <label for="email" class="label">Email</label>
                                <div class="control has-icons-left">
                                    <input type="email" name="email" id="" class="input">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-envelope"></i>
                                    </span>
                                </div>
                            </div>

                            <div class="field">
                                <label for="password1" class="label">Password</label>
                                <div class="control has-icons-left">
                                    <input type="password" name="password1" id="" class="input">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-key"></i>
                                    </span>
                                </div>
                            </div>

                            <div class="field">
                                <label for="password2" class="label">Confirm Your Password</label>
                                <div class="control has-icons-left">
                                    <input type="password" name="password2" id="" class="input">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-key"></i>
                                    </span>
                                </div>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <button type="submit" class="button is-primary">Submit</button>
                                </div>
                            </div>

                        </form>
                        <hr>
                        <router-link to="/login">Click here</router-link> to login
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    methods:{
        onSubmit(){
            console.log("This is submitted")
        }
    }
}
</script>