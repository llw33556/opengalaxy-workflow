<template>
  <div class="dashboard-container">
    <el-tabs v-model="activeName" @tab-click="handleClick" style="margin-left: 10px">
      <el-tab-pane label="日常工具地址大全" name="first">
        <el-table
          :data="tableData"
          style="width: 90%;margin-left: 3%"
          :row-class-name="tableRowClassName">
          <el-table-column
            prop="name"
            label="简称"
            >
          </el-table-column>
          <el-table-column
            prop="url"
            label="url"
            >
            <template slot-scope="scope">
              <span class="link-type" @click="handleGoUrl(scope.row.url)">{{ scope.row.url }}</span>
            </template>
          </el-table-column>
          <el-table-column
            prop="detail"
            label="描述">
          </el-table-column>
        </el-table>
        </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: 'Dashboard',
    data() {
      return {
        currentRole: 'adminDashboard',
        activeName: 'first',
        tableData: [{
          name: '项目管理工具',
          url: 'http://jira.baidu.com',
          detail: '根据页面提示联系项目经历开通权限',
        }, {
          name: 'GITLAB代码管理',
          url: 'http://gitlab.baidu.com/',
          detail: '代码管理系统'
        }, {
          name: '私服nexus工具',
          url: 'http://nexus.baidu.com/',
          detail: 'maven仓库私服工具nexus',
        }, {
          name: 'Jenkins代码发布工具',
          url: 'http://jenkins.dev.baidu.com/',
          detail: '代码发布工具'
        }, {
          name: 'API文档(新)',
          url: 'http://apims.baidu.com/',
          detail: 'api接口文档'
        }, {
          name: 'API文档(旧)',
          url: 'http://abc.baidu.com/',
          detail: 'api接口文档'
        }, {
          name: '堡垒机(主)',
          url: 'http://baoleim.ops.baidu.com/',
          detail: '堡垒机(主)'
        }, {
          name: '堡垒机(从)',
          url: 'http://baoleis.ops.baidu.com/',
          detail: '堡垒机(从)'
        }, {
          name: '生产环境中间件监控平台',
          url: 'http://monitor.baidu.com/',
          detail: '生产环境所有中间件监控集中平台'
        }, {
          name: '分布式调用中心',
          url: 'http://zc.baidu.com/',
          detail: '分布式调用中心'
        }]
      }
    },
    computed: {
      ...mapGetters([
        'roles'
      ])
    },
    created() {
      if (!this.roles.includes('admin')) {
        this.currentRole = 'editorDashboard'
      }
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      },
      handleGoUrl(url) {
        window.open(url, '_blank');
      },
      tableRowClassName({row, rowIndex}) {
        if (rowIndex === 1) {
          return 'warning-row';
        } else if (rowIndex === 3) {
          return 'success-row';
        } else if (rowIndex === 5) {
          return 'info-row';
        } else if (rowIndex === 8) {
          return 'transp-row';
        }else if (rowIndex === 11) {
          return 'zzz-row';
        }
        return '';
      }
    }
  }
</script>
<style>
  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }
  .el-table .info-row {
    background: #ccffff;
  }
  .el-table .transp-row {
    background: #cce5ff;
  }
  .el-table .zzz-row {
    background: #ffccff;
  }
</style>
