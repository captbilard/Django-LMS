<template>
    <nav class="navbar is-primary" role="navigation" aria-label="main navigation" style="min-height:5rem;">
        <div class="navbar-brand" >
            <a href="/" class="navbar-item is-size-4">LMS</a>
        </div>

        <div class="navbar-menu" id="navbar-item">
            <div class="navbar-start">
                <a href="/" class="navbar-item">Home</a>
                <a href="/about" class="navbar-item">About</a>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="$store.state.user.isAuthenticated">
                            <router-link to="/dashboard/my-account" class="button is-warning"> My Dashboard</router-link>
                        </template>
                        <template v-else>
                            <a href="/sign-up" class="button is-primary"><strong>Sign Up</strong></a>
                            <a href="/login" class="button is-light">Login</a>
                        </template>
                    </div>
                </div>
            </div>
        
        </div>
    </nav>
</template>