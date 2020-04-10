<template>
  <div class="content-section">
        <section class="hero is-white is-fullheight-with-navbar">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title has-text-centered is-unselectable">404: Page Not Found</h1>
                    <br/>
                    <div class="subtitle has-text-centered">
                        <div class="button is-dark" @click="$router.go(-1)">
                        Return to Previous Page</div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>