<template>
  <div>
    <div class="h-screen overflow-hidden relative flex flex-row">
  <div class="relative flex flex-col bg-clip-border bg-white text-gray-700 h-screen max-w-[20rem] p-4 shadow-xl shadow-blue-gray-900/5">
    <div class="mb-2 p-4">
      <h5 class="block antialiased tracking-normal font-sans text-2xl font-semibold leading-snug text-gray-900">Payroll Management</h5>
      <h3 class="antialiased text-xl">{{ role }}</h3>
    </div>
    <nav class="flex flex-col gap-1 min-w-[240px] p-2 font-sans text-base font-normal text-gray-700">
      <div v-for="data in links" :key="data.path" class="w-full">
        <RouterLink
          :to="`/${data.path}`"
          role="button"
          tabindex="0"
          class="flex items-center w-full p-3 rounded-lg text-start leading-tight transition-all hover:bg-blue-50 hover:bg-opacity-80 focus:bg-blue-50 focus:bg-opacity-80 active:bg-gray-50 active:bg-opacity-80 hover:text-blue-900 focus:text-blue-900 active:text-blue-900 outline-none"
        >
          <div class="flex-shrink-0 mr-4">
            <i v-if="data.name === 'Manage Users'" class="fa-solid fa-address-book"></i>
            <i v-else-if="data.name === 'Payroll Slip'" class="fa-solid fa-file-invoice"></i>
            <i v-else-if="data.name === 'Overtime'" class="fa-solid fa-stopwatch"></i>
            <i v-else-if="data.name === 'Statistics'" class="fa-solid fa-square-poll-vertical"></i>
            <i v-else-if="data.name === 'Profile'" class="fa-solid fa-id-badge"></i>
            <i v-else class="fa-solid fa-question fa-bounce"></i>
          </div>
          <span class="flex-grow">{{ data.name }}</span>
        </RouterLink>
      </div>
      <!-- <div role="button" @click="currentTab = 'ReadSlip'" tabindex="0" class="flex items-center w-full p-3 rounded-lg text-start leading-tight transition-all hover:bg-blue-50 hover:bg-opacity-80 focus:bg-blue-50 focus:bg-opacity-80 active:bg-gray-50 active:bg-opacity-80 hover:text-blue-900 focus:text-blue-900 active:text-blue-900 outline-none">
        <div class="grid place-items-center mr-4">
          <i class=></i>        
        </div>
        Payroll Slip
      </div>
      <div role="button" @click="currentTab = 'OvertimeOwner'" tabindex="0" class="flex items-center w-full p-3 rounded-lg text-start leading-tight transition-all hover:bg-blue-50 hover:bg-opacity-80 focus:bg-blue-50 focus:bg-opacity-80 active:bg-blue-50 active:bg-opacity-80 hover:text-blue-900 focus:text-blue-900 active:text-blue-900 outline-none">
        <div class="grid place-items-center mr-4">
          <i class="fa-solid fa-stopwatch"></i>
        </div>Overtime<div class="grid place-items-center ml-auto justify-self-end">
        </div>
        <div class="relative grid items-center font-sans font-bold uppercase whitespace-nowrap select-none bg-blue-500/20 text-blue-900 py-1 px-2 text-xs rounded-full" style="opacity: 1;">
            <span class="">14</span>
          </div>
      </div>
      <div role="button" tabindex="0" @click="currentTab = 'Statistics'" class="flex items-center w-full p-3 rounded-lg text-start leading-tight transition-all hover:bg-blue-50 hover:bg-opacity-80 focus:bg-blue-50 focus:bg-opacity-80 active:bg-blue-50 active:bg-opacity-80 hover:text-blue-900 focus:text-blue-900 active:text-blue-900 outline-none">
        <div class="grid place-items-center mr-4">
          <i class="fa-solid fa-square-poll-vertical"></i>
        </div>Statistics 
      </div>
      <div role="button" tabindex="0" @click="currentTab = 'Profile'" class="flex items-center w-full p-3 rounded-lg text-start leading-tight transition-all hover:bg-blue-50 hover:bg-opacity-80 focus:bg-blue-50 focus:bg-opacity-80 active:bg-blue-50 active:bg-opacity-80 hover:text-blue-900 focus:text-blue-900 active:text-blue-900 outline-none">
        <div class="grid place-items-center mr-4">
          <i class="fa-solid fa-id-badge"></i>
        </div>Profile
      </div> -->
      <div role="button" @click="toggleModal" tabindex="0" class="flex items-center w-full p-3 rounded-lg text-start leading-tight transition-all hover:bg-blue-50 hover:bg-opacity-80 focus:bg-blue-50 focus:bg-opacity-80 active:bg-blue-50 active:bg-opacity-80 hover:text-blue-900 focus:text-blue-900 active:text-blue-900 outline-none">
        <div class="grid place-items-center mr-4">
          <i class="fa-solid fa-power-off"></i>
        </div>Log Out
      </div>
      <BaseModal
            :modalActive="modalActive"
            @close-modal="toggleModal"
        >
            <div>
              <div class="text-center p-3 flex-auto justify-center leading-6">
                <i class="fa-solid fa-person-through-window text-7xl px-32"></i>
                <h2 class="text-2xl font-bold mt-6">Are you sure?</h2>
                <p class="text-md text-gray-500 px-8 mt-4">
                  Do you really want to log out?
                </p>
                <RouterLink to="/login">
                  <button
                  class="text-black mt-8 border shadow-md bg-canvas-secondary py-2 px-6 mr-6"
                  @click="handleLogoutButton"
                >
                  Log Out
                </button>
              </RouterLink>
              <button
                class="text-white mt-8 shadow-md border bg-canvas-primary py-2 px-6"
                @click="toggleModal"
              >
                Cancel
              </button>
              </div>
            </div>
        </BaseModal>
    </nav>
  </div>
  <!-- component -->
  <div class="">
    <component :is="currentTab"></component>
    <!-- <UserManagement /> -->
    <!-- <OvertimeOwner /> -->
    <!-- <OvertimeEmployee /> -->
    <!-- <Profile />   -->
    <!-- <Statistics /> -->
    <!-- <ReadSlip /> -->
  </div>  
</div>
</div>

  </template>
  
  <script>

  </script>

  <script setup>
  import BaseModal from './BaseModal.vue'
  import { ref } from 'vue'
  import UserManagement from './UserManagement.vue'
  import OvertimeOwner from './OvertimeOwner.vue'
  import OvertimeEmployee from './OvertimeEmployee.vue'
  import Profile from './Profile.vue'
  import Statistics from './Statistics.vue'
  import ReadSlip from './ReadSlip.vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios';
  import VueCookies from 'vue-cookies';


  // import Vue from 'vue'; import VueCookies from 'vue-cookies'; Vue.use(VueCookies);

  const router = useRouter()
  const modalActive = ref(null);
  const toggleModal = () => {
      modalActive.value = !modalActive.value;
  };
  var param = '';

  var role = VueCookies.get("role")
  var links = []
  if (role === "owner") {
    links.push({
        name: "Manage Users",
        path: "UserManagement",
      }),
      links.push({
        name: "Payroll Slip",
        path: "ReadSlip",
      })
      links.push({
        name: "Overtime",
        path: "OvertimeOwner",
        icon: "fa-solid fa-stopwatch",
      })
      links.push({
        name: "Statistics",
        path: "Statistics",
        icon: "fa-solid fa-square-poll-vertical",
      })
      links.push({
        name: "Profile",
        path: "Profile",
        icon: "fa-solid fa-id-badge",
      })
  } else if (role === "finance"){
    links.push({
        name: "Payroll Slip",
        path: "ReadSlip",
        icon: "fa-solid fa-file-invoice",
      })
      links.push({
        name: "Overtime",
        path: "OvertimeOwner",
        icon: "fa-solid fa-stopwatch", 
      })
      links.push({
        name: "Profile",
        path: "Profile",
        icon: "fa-solid fa-id-badge",
      })
  } else if (role === "employee") {
      links.push({
        name: "Payroll Slip",
        path: "ReadSlip",
        icon: "fa-solid fa-file-invoice",
      })
      links.push({
        name: "Overtime",
        path: "OvertimeEmployee",
        icon: "fa-solid fa-stopwatch", 
      })
      links.push({
        name: "Profile",
        path: "Profile",
        icon: "fa-solid fa-id-badge",
      })
    }

  defineOptions({
    components: {
      UserManagement,
      OvertimeOwner,
      OvertimeEmployee,
      Profile,
      Statistics,
      ReadSlip,
    },
    data() {
      return {
        currentTab: 'Profile',
        tabs: [ 'UserManagement',
                'OvertimeOwner',
                'OvertimeEmployee',
                'Profile',
                'Statistics',
                'ReadSlip',
              ],
      };
    },
    components: {

    },
    methods: {
      async logout() {
          try {
              const path = 'http://localhost:5001/token/remove';
              const response = await axios.post(path, {}, {withCredentials: true,});
              VueCookies.remove('role');
              console.log('Logout successful:', response.data);
          } catch (error) {
              console.error('Error logging in:', error.response?.data || error.message);
          }
      },
      handleClickTab(param) {
        this.router.replace({ path: '/aa' + param })
      },
      handleLogoutButton() {
        this.logout();
        // VueCookies.remove('access_token_cookie'); //doesn't work?
        // VueCookies.remove('csrf_access_token');
      }
    },
  });

  </script>