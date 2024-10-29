const getOptionChart3 = () => {
    return {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['Efectivo', 'Transferencia', 'T. Débito','T. Crédito'] 
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            right: 'left',
            top: 'center',
            feature: {
                mark: { show: true },
                dataView: { show: false, readOnly: false },
                magicType: { show: false, type: ['line', 'bar', 'stack'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: { show: true },
                data: periodoVta
            }
        ],
        yAxis: [
            {
                type: 'value',
            }
        ],
        series: [
            {
                name: 'Efectivo', 
                type: 'bar',
                barGap: 0,
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [efectivo_vta]  
            },
            {
                name: 'Transferencia',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [transferencia_vta]  
            },
            {
                name: 'T. Débito',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [tarjeta_debito_vta]  
            },            
            {
                name: 'T. Crédito',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [tarjeta_credito_vta]  
            },
        ]
    };
};

const initCharts = () => {
    const chart1 = echarts.init(document.getElementById('chart3'));
    chart1.setOption(getOptionChart3());
};

window.addEventListener("load", () => {
    initCharts();
});
