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
        <div class="bg-white overflow-auto h-[calc(100vh)] max-w-full w-[calc(80vw)]">
            <!-- Invoice -->
            <div class="px-4 sm:px-6 lg:px-8 py-4 mx-auto">
            <!-- Grid -->
            <div class="mb-5 pb-5 flex justify-between items-center border-b border-gray-200">
                <div>
                <h2 class="text-2xl font-semibold text-gray-800">Salary Slip</h2>
                </div>
                <!-- Col -->

                <div class="inline-flex gap-x-2">
                <a class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none focus:outline-none focus:bg-gray-50" href="#">
                <svg class="shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>
                    Save to PDF
                </a>
                <a class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 focus:outline-none focus:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none" href="#">
                    <svg class="shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect width="12" height="8" x="6" y="14"/></svg>
                    Print
                </a>
                </div>
                <!-- Col -->
            </div>
            <!-- End Grid -->

            <!-- Grid -->
            <div class="grid md:grid-cols-2 gap-3">
                <div>
                <div class="grid space-y-3">
                    <dl class="flex flex-col sm:flex-row gap-x-3 text-sm">
                    <dt class="min-w-36 max-w-[200px] text-gray-500">
                        Employee:
                    </dt>
                    <dd class="text-gray-800">
                        Drh. Endang Dwi Astuti
                    </dd>
                    </dl>

                    <dl class="flex flex-col sm:flex-row gap-x-3 text-sm">
                    <dt class="min-w-36 max-w-[200px] text-gray-500">
                        Office address:
                    </dt>
                    <dd class="font-medium text-gray-800">
                        <span class="block font-semibold">ABC Pet Shop & Clinic</span>
                        <address class="not-italic font-normal">
                        Business Centre, Ruko Palagan Blok B No. 7<br>
                        Sariharjo, Ngaglik, Sleman 55581<br>
                        Yogyakarta, Indonesia<br>
                        </address>
                    </dd>
                    </dl>

                    <!-- <dl class="flex flex-col sm:flex-row gap-x-3 text-sm">
                    <dt class="min-w-36 max-w-[200px] text-gray-500">
                        Shipping details:
                    </dt>
                    <dd class="font-medium text-gray-800">
                        <span class="block font-semibold">Sara Williams</span>
                        <address class="not-italic font-normal">
                        280 Suzanne Throughway,<br>
                        Breannabury, OR 45801,<br>
                        United States<br>
                        </address>
                    </dd>
                    </dl> -->
                </div>
                </div>
                <!-- Col -->

                <div>
                <div class="grid space-y-3">
                    <dl class="flex flex-col sm:flex-row gap-x-3 text-sm">
                    <dt class="min-w-36 max-w-[200px] text-gray-500">
                        Slip ID:
                    </dt>
                    <dd class="font-medium text-gray-800">
                        ABC-1024-EDA
                    </dd>
                    </dl>

                    <dl class="flex flex-col sm:flex-row gap-x-3 text-sm">
                    <dt class="min-w-36 max-w-[200px] text-gray-500">
                        Pay Period:
                    </dt>
                    <dd class="font-medium text-gray-800">
                        Oktober 2024
                    </dd>
                    </dl>

                    <dl class="flex flex-col sm:flex-row gap-x-3 text-sm">
                    <dt class="min-w-36 max-w-[200px] text-gray-500">
                        Payment method:
                    </dt>
                    <dd class="font-medium text-gray-800">
                        BCA - 0374315777
                    </dd>
                    </dl>
                </div>
                </div>
                <!-- Col -->
            </div>
            <!-- End Grid -->

            <!-- Table -->
            <div class="mt-6 border border-gray-200 p-4 rounded-lg space-y-4">
                <div class="hidden sm:grid sm:grid-cols-5">
                <div class="sm:col-span-2 text-xs font-medium text-gray-500 uppercase">Earnings</div>
                <div class="text-start text-xs font-medium text-gray-500 uppercase">Qty</div>
                <div class="text-start text-xs font-medium text-gray-500 uppercase">Rate</div>
                <div class="text-end text-xs font-medium text-gray-500 uppercase">Amount</div>
                </div>

                <div class="hidden sm:block border-b border-gray-200"></div>

                <div class="grid grid-cols-3 sm:grid-cols-5 gap-2">
                <div class="col-span-full sm:col-span-2">
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Earnings</h5>
                    <p class="font-medium text-gray-800">Gaji Pokok</p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Qty</h5>
                    <p class="text-gray-800"></p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Rate</h5>
                    <p class="text-gray-800"></p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Amount</h5>
                    <p class="sm:text-end text-gray-800">Rp 12.000.000</p>
                </div>
                </div>

                <div class="sm:hidden border-b border-gray-200"></div>

                <div class="grid grid-cols-3 sm:grid-cols-5 gap-2">
                <div class="col-span-full sm:col-span-2">
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Item</h5>
                    <p class="font-medium text-gray-800">Tunjangan Makan</p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Qty</h5>
                    <p class="text-gray-800"></p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Rate</h5>
                    <p class="text-gray-800"></p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Amount</h5>
                    <p class="sm:text-end text-gray-800">Rp 2.500.000</p>
                </div>
                </div>

                <div class="sm:hidden border-b border-gray-200"></div>

                <div class="grid grid-cols-3 sm:grid-cols-5 gap-2">
                <div class="col-span-full sm:col-span-2">
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Item</h5>
                    <p class="font-medium text-gray-800">Transport</p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Qty</h5>
                    <p class="text-gray-800"></p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Rate</h5>
                    <p class="text-gray-800"></p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Amount</h5>
                    <p class="sm:text-end text-gray-800">Rp 2.000.000</p>
                </div>
                </div>

                <div class="sm:hidden border-b border-gray-200"></div>

                <div class="grid grid-cols-3 sm:grid-cols-5 gap-2">
                <div class="col-span-full sm:col-span-2">
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Item</h5>
                    <p class="font-medium text-gray-800">Performance</p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Qty</h5>
                    <p class="text-gray-800"></p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Rate</h5>
                    <p class="text-gray-800"></p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Amount</h5>
                    <p class="sm:text-end text-gray-800">Rp 1.000.000</p>
                </div>
                </div>

                <div class="sm:hidden border-b border-gray-200"></div>

                <div class="grid grid-cols-3 sm:grid-cols-5 gap-2">
                <div class="col-span-full sm:col-span-2">
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Item</h5>
                    <p class="font-medium text-gray-800">Overtime</p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Qty</h5>
                    <p class="text-gray-800">18 Hours</p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Rate</h5>
                    <p class="text-gray-800">Rp 100.000</p>
                </div>
                <div>
                    <h5 class="sm:hidden text-xs font-medium text-gray-500 uppercase">Amount</h5>
                    <p class="sm:text-end text-gray-800">Rp 1.800.000</p>
                </div>
                </div>
            </div>
            <!-- End Table -->

            <!-- Flex -->
            <div class="mt-8 flex sm:justify-end">
                <div class="w-full max-w-2xl sm:text-end space-y-2">
                <!-- Grid -->
                <div class="grid grid-cols-2 sm:grid-cols-1 gap-3 sm:gap-2">
                    <dl class="grid sm:grid-cols-5 gap-x-3 text-sm">
                    <dt class="col-span-3 text-gray-500">Subotal:</dt>
                    <dd class="col-span-2 font-medium text-gray-800">Rp 19.300.000</dd>
                    </dl>

                    <dl class="grid sm:grid-cols-5 gap-x-3 text-sm">
                    <dt class="col-span-3 text-gray-500">Tax:</dt>
                    <dd class="col-span-2 font-medium text-gray-800">Rp 1.930.000</dd>
                    </dl>

                    <dl class="grid sm:grid-cols-5 gap-x-3 text-sm">
                    <dt class="col-span-3 text-gray-500">Deduction:</dt>
                    <dd class="col-span-2 font-medium text-gray-800">Rp 0</dd>
                    </dl>

                    <br>

                    <dl class="grid sm:grid-cols-5 gap-x-3 text-xl font-semibold">
                    <dt class="col-span-3 text-gray-900 ">Net Salary:</dt>
                    <dd class="col-span-2 text-gray-900 font-semibold">Rp 17.370.000</dd>
                    </dl>
                </div>
                <!-- End Grid -->
                </div>
            </div>
            <!-- End Flex -->
            </div>
            <!-- End Invoice -->
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