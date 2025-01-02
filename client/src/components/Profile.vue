<template>
<div class="flex h-screen bg-canvas-primary">
    <div>
      <SiteNavigation />
    </div>
    <div class="flex-1 h-full max-w-screen w-[calc(80vw)]">
    <div class="relative flex flex-col w-full h-full text-slate-700 bg-white shadow-md bg-clip-border">
        <div class="relative mx-4 mt-4 overflow-hidden text-slate-700 bg-white rounded-none bg-clip-border">
          <div class="flex items-center justify-between">
    <div>
        <div class="bg-white overflow-auto shadow h-[calc(100vh)] max-w-full w-[calc(80vw)]">
            <div class="px-4 py-5 sm:px-6">
                <h3 class="text-xl leading-6 font-extrabold text-gray-900">
                    Your Profile
                </h3>
                <p class="mt-1 max-w-2xl text-sm text-gray-500">
                    Basic information should be listed here
                </p>
                <p class="mt-1 max-w-2xl text-xs text-gray-500">
                    If there is any incorrect data please report to Owner.
                </p>
            </div>
            <div class="border-t border-gray-200 px-4 py-5 sm:p-0">
                <dl class="sm:divide-y sm:divide-gray-200">
                    <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-base font-bold text-slate-950">
                            Identity
                        </dt>
                    </div>
                    <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">
                            Full name
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            Drh. Endang Dwi Astuti
                        </dd>
                    </div>
                    <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">
                            Email address
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            drhendangdwiastuti@gmail.com
                        </dd>
                    </div>
                    <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">
                            Phone number
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            085640063500
                        </dd>
                    </div>
                    <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">
                            Address
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            Apartemen B Residence Grogol<br>
                            Daan Mogot Rd No.79, RT.5/RW.1, Duri Kepa, Kebonjeruk, West Jakarta City, Jakarta 11510
                        </dd>
                    </div>
                    <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">
                            Function
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            Dokter Hewan
                        </dd>
                    </div>
                    <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">
                            Employment Date
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            20/10/2020
                        </dd>
                    </div>
                    <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-base font-bold text-slate-950">
                            Payment Information
                        </dt>
                    </div>
                    <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-gray-500">
                            Account
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            BCA<br>
                            0374315777
                        </dd>
                    </div>
                </dl>
            </div>
        </div>
    </div>
</div>
            </div>
        </div>
    </div>
    </div>

</template>

<script setup>
import SiteNavigation from './SiteNavigation.vue'

</script>

<style lang="scss" scoped>

</style>