import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import SignUp from "../views/SignUp.vue";
import Login from "../views/Login.vue";

import Courses from "../views/Courses.vue";
import Course from "../views/Course.vue";

import MyAccount from "../views/dashboard/MyAccount.vue";
import SuccessPage from "../views/Stripe_Payments/SuccessPage.vue";
import CancelPage from "../views/Stripe_Payments/CancelPage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/dashboard/my-account",
    name: "MyAccount",
    component: MyAccount,
  },
  {
    path: "/courses",
    name: "Courses",
    component: Courses,
  },
  {
    path: "/courses/:slug",
    name: "Course",
    component: Course,
  },
  {
    path: "/success",
    name: "SuccessPage",
    component: SuccessPage,
  },
  {
    path: "/cancelled",
    name: "CancelPage",
    component: CancelPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
