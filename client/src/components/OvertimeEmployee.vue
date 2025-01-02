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
                   <h3 class="text-lg font-extrabold text-slate-800">Overtime Request Form</h3>
                   <p class="text-slate-500">Request your overtime from here</p>
               </div>
            </div>
       </div>
       <form class="px-8 my-12">
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-first-name">
                Your Name
            </label>
            <input class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="grid-first-name" type="text" placeholder="Drh. Endang Dwi Astuti" disabled>
            </div>
            <div class="w-full md:w-1/2 px-3">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-last-name">
                Employee Code
            </label>
            <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-last-name" type="text" placeholder="EDA2020" disabled>
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-2">
            <div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-city">
                Duration (hours)
            </label>
            <input class="appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-city" type="number" min="0" placeholder="0">
            </div>
        </div>
        </form>
       <div class="mt-8 flex items-center justify-between p-3 mr-7">
           <p class="block text-sm text-slate-500">
           
           </p>
           <div class="flex gap-1">
           <button
                @click="toggleModal"
               class="rounded border bg-green-500 border-slate-300 py-2.5 px-3 text-center text-xs font-semibold text-white transition-all hover:opacity-75 focus:ring focus:ring-slate-300 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
               type="button">
               Request Approval
           </button>
           <BaseModal
                :modalActive="modalActive"
                @close-modal="toggleModal"
            >
                <div>
                <div class="text-center p-3 flex-auto justify-center leading-6">
                    <i class="fa-solid fa-hand fa-beat fa-2xl text-7xl px-32"></i>
                    <h2 class="text-2xl font-bold mt-6">Wait...</h2>
                    <p class="text-md text-gray-500 px-8 mt-4">
                    Do you want to check your entry first?
                    </p>
                    <RouterLink to="/">
                    <button
                    class="text-black mt-8 border shadow-md bg-canvas-secondary py-2 px-6 mr-6"
                    @click="toggleModal"
                    >
                    Submit
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
           </div>
       </div>
       </div>
    </div>
    </div>
</template>

<script setup>
import BaseModal from './BaseModal.vue'
import { ref } from 'vue'
import SiteNavigation from './SiteNavigation.vue'


const modalActive = ref(null);
  const toggleModal = () => {
      modalActive.value = !modalActive.value;
  };
  defineEmits(["close-modal"]);
</script>

<style lang="scss" scoped>

</style>