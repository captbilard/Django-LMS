<template>
    <div class="myAccount">
        <div class="hero is-primary">
            <div class="hero-body has-text-centered">
                <p class="title">My Account</p>
            </div>
        </div>

        <section class="section">
            <button class="button is-danger" v-on:click="logout">Logout</button>
        </section>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    methods:{
        logout: function (){
            delete axios.defaults.headers.common["Authorization"]

            //remove token from 
            localStorage.removeItem('token')

            //remove from store using mutations
            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script>