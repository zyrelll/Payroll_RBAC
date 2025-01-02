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
                   <h3 class="text-lg font-extrabold text-slate-800">Overtime Request List</h3>
                   <p class="text-slate-500">Review each request before approval</p>
               </div>
            </div>
       </div>
       <div class="p-0 overflow-hidden">
           <table class="w-full mt-4 text-left table-auto min-w-max">
           <thead>
               <tr>
               <th
                   class="p-4 transition-colors cursor-pointer border-y border-slate-200 bg-slate-50 hover:bg-slate-100">
                   <p
                   class="flex items-center justify-between gap-2 font-sans text-sm font-normal leading-none text-slate-500">
                   Employees
                   </p>
               </th>
               <th
                   class="p-4 transition-colors cursor-pointer border-y border-slate-200 bg-slate-50 hover:bg-slate-100">
                   <p
                   class="flex items-center justify-between gap-2 font-sans text-sm font-normal leading-none text-slate-500">
                   Function
                   </p>
               </th>
               <th
                   class="p-4 transition-colors cursor-pointer border-y border-slate-200 bg-slate-50 hover:bg-slate-100">
                   <p
                   class="flex items-center justify-between gap-2 font-sans text-sm  font-normal leading-none text-slate-500">
                   Status
                   </p>
               </th>
               <th
                   class="p-4 transition-colors cursor-pointer border-y border-slate-200 bg-slate-50 hover:bg-slate-100">
                   <p
                   class="flex items-center justify-between gap-2 font-sans text-sm  font-normal leading-none text-slate-500">
                   Duration
                   </p>
               </th>
               <th
                   class="p-4 transition-colors cursor-pointer border-y border-slate-200 bg-slate-50 hover:bg-slate-100">
                   <p
                   class="flex items-center justify-between gap-2 font-sans text-sm  font-normal leading-none text-slate-500">
                   </p>
               </th>
               <th
                   class="p-4 transition-colors cursor-pointer border-y border-slate-200 bg-slate-50 hover:bg-slate-100">
                   <p
                   class="flex items-center justify-between gap-2 font-sans text-sm  font-normal leading-none text-slate-500">
                   </p>
               </th>
               </tr>
           </thead>
           <tbody>
               <tr>
               <td class="p-4 border-b border-slate-200">
                   <div class="flex items-center gap-3">
                   <img src="https://demos.creative-tim.com/test/corporate-ui-dashboard/assets/img/team-2.jpg"
                       alt="Alexa Liras" class="relative inline-block h-9 w-9 !rounded-full object-cover object-center" />
                   <div class="flex flex-col">
                       <p class="text-sm font-semibold text-slate-700">
                       Vanya Kurniadi
                       </p>
                       <p
                       class="text-sm text-slate-500">
                       vanyakun@gmail.com
                       </p>
                   </div>
                   </div>
               </td>
               <td class="p-4 border-b border-slate-200">
                   <div class="flex flex-col">
                   <p class="text-sm font-semibold text-slate-700">
                       Groomer
                   </p>
                   </div>
               </td>
               <td class="p-4 border-b border-slate-200">
                   <div class="w-max">
                   <div
                       class="relative grid items-center px-2 py-1 font-sans text-xs font-bold uppercase rounded-md select-none whitespace-nowrap bg-slate-100 text-slate-500">
                       <span class="">waiting</span>
                   </div>
                   </div>
               </td>
               <td class="p-4 border-b border-slate-200">
                   <p class="text-sm text-slate-500">
                   3 Hour(s)
                   </p>
               </td>
               <td class="p-4 border-b border-slate-200">
                   <button
                   @click="toggleModalAccept"
                   class="relative h-10 max-h-[40px] w-10 max-w-[40px] select-none rounded-lg text-center align-middle font-sans text-xs font-medium uppercase text-slate-900 transition-all hover:bg-slate-900/10 active:bg-slate-900/20 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                   type="button">
                   <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
                       <i class="fa-solid fa-circle-check fa-xl" style="color: #63E6BE;"></i>
                   </span>
                   </button>
               </td>
               <td class="pr-4 border-b border-slate-200">
                   <button
                   @click="toggleModalReject"
                   class="relative h-10 max-h-[40px] w-10 max-w-[40px] select-none rounded-lg text-center align-middle font-sans text-xs font-medium uppercase text-slate-900 transition-all hover:bg-slate-900/10 active:bg-slate-900/20 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                   type="button">
                   <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
                    <i class="fa-solid fa-circle-xmark fa-xl" style="color: #ec3c7a;"></i></span>
                   </button>
               </td>
               </tr>
               <tr>
               <td class="p-4 border-b border-slate-200">
                   <div class="flex items-center gap-3">
                   <img src="https://demos.creative-tim.com/test/corporate-ui-dashboard/assets/img/team-1.jpg"
                       alt="Drh. Endang Dwi Astuti"
                       class="relative inline-block h-9 w-9 !rounded-full object-cover object-center" />
                   <div class="flex flex-col">
                       <p class="text-sm font-semibold text-slate-700">
                        Drh. Endang Dwi Astuti
                       </p>
                       <p
                       class="text-sm text-slate-500">
                       drhendangdwiastuti@gmail.com
                       </p>
                   </div>
                   </div>
               </td>
               <td class="p-4 border-b border-slate-200">
                   <div class="flex flex-col">
                   <p class="text-sm font-semibold text-slate-700">
                       Dokter Hewan
                   </p>
                   </div>
               </td>
               <td class="p-4 border-b border-slate-200">
                   <div class="w-max">
                   <div
                       class="relative grid items-center px-2 py-1 font-sans text-xs font-bold uppercase rounded-md select-none whitespace-nowrap bg-slate-100 text-slate-500">
                       <span class="">waiting</span>
                   </div>
                   </div>
               </td>
               <td class="p-4 border-b border-slate-200">
                   <p class="text-sm text-slate-500">
                   2 Hour(s)
                   </p>
               </td>
               <td class="p-4 border-b border-slate-200">
                   <button
                   @click="toggleModalAccept"
                   class="relative h-10 max-h-[40px] w-10 max-w-[40px] select-none rounded-lg text-center align-middle font-sans text-xs font-medium uppercase text-slate-900 transition-all hover:bg-slate-900/10 active:bg-slate-900/20 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                   type="button">
                   <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
                       <i class="fa-solid fa-circle-check fa-xl" style="color: #63E6BE;"></i>
                   </span>
                   </button>
               </td>
               <td class="pr-4 border-b border-slate-200">
                   <button
                   @click="toggleModalReject"
                   class="relative h-10 max-h-[40px] w-10 max-w-[40px] select-none rounded-lg text-center align-middle font-sans text-xs font-medium uppercase text-slate-900 transition-all hover:bg-slate-900/10 active:bg-slate-900/20 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                   type="button">
                   <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
                    <i class="fa-solid fa-circle-xmark fa-xl" style="color: #ec3c7a;"></i></span>
                   </button>
               </td>
               </tr>
           </tbody>
           </table>
       </div>
       <div class="flex items-center justify-between p-3">
           <p class="block text-sm text-slate-500">
           Page 1 of 10
           </p>
           <div class="flex gap-1">
           <button
               class="rounded border border-slate-300 py-2.5 px-3 text-center text-xs font-semibold text-slate-600 transition-all hover:opacity-75 focus:ring focus:ring-slate-300 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
               type="button">
               Previous
           </button>
           <button
               class="rounded border border-slate-300 py-2.5 px-3 text-center text-xs font-semibold text-slate-600 transition-all hover:opacity-75 focus:ring focus:ring-slate-300 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
               type="button">
               Next
           </button>
           </div>
       </div>
       <BaseModal
            :modalActive="modalActiveAccept"
            @close-modal="toggleModalAccept"
        >
            <div>
              <div class="text-center p-3 flex-auto justify-center leading-6">
                <i class="fa-solid fa-person-through-window text-7xl px-32"></i>
                <h2 class="text-2xl font-bold mt-6">Are you sure?</h2>
                <p class="text-md text-gray-500 px-8 mt-4">
                  Accept overtime request?
                </p>
                  <button
                  class="text-white mt-8 border shadow-md bg-green-500 py-2 px-6 mr-6"
                  @click="toggleModalAccept"
                >
                  Accept
                </button>
              <button
                class="text-white mt-8 shadow-md border bg-canvas-primary py-2 px-6"
                @click="toggleModalAccept"
              >
                Cancel
              </button>
              </div>
            </div>
        </BaseModal>
        <BaseModal
            :modalActive="modalActiveReject"
            @close-modal="toggleModalReject"
        >
            <div>
              <div class="text-center p-3 flex-auto justify-center leading-6">
                <i class="fa-solid fa-person-through-window text-7xl px-32"></i>
                <h2 class="text-2xl font-bold mt-6">Are you sure?</h2>
                <p class="text-md text-gray-500 px-8 mt-4">
                  Reject overtime request?
                </p>
                  <button
                  class="text-white mt-8 border shadow-md bg-red-500 py-2 px-6 mr-6"
                  @click="toggleModalReject"
                >
                  Reject
                </button>
              <button
                class="text-white mt-8 shadow-md border bg-canvas-primary py-2 px-6"
                @click="toggleModalReject"
              >
                Cancel
              </button>
              </div>
            </div>
        </BaseModal>
       </div>
    </div>
    </div>
</template>

<script setup>
import BaseModal from './BaseModal.vue'
import { ref } from "vue"
import SiteNavigation from './SiteNavigation.vue'
const modalActiveAccept = ref(null);
const modalActiveReject = ref(null);
const toggleModalAccept = () => {
    modalActiveAccept.value = !modalActiveAccept.value;
};
const toggleModalReject = () => {
    modalActiveReject.value = !modalActiveReject.value;
};
defineEmits(["close-modal"]);

</script>

<style lang="scss" scoped>

</style>