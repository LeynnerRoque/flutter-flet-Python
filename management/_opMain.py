from enterprises import enterprise_operation as enterprise
from jobs import jobs_operation as job
from local import local_operation as local
from peoples import peoples_operation as people

def select_all_peoples():
 people.peoples_operation.select_all()

def add_peoples():
    people.peoples_operation.add_peoples()

def update_peoples():
    people.peoples_operation.update_peoples()

def add_people_on_work():
    people.peoples_operation.add_people_on_work()

def add_people_on_local():
    people.peoples_operation.add_people_on_local()

# Jobs Operation
def select_all_jobs():
    job.jobs_operation.select_all()

def create_job():
    job.jobs_operation.create_job()

def update_job():
    job.jobs_operation.update_jobs()

def add_job_enterprise():
    job.jobs_operation.add_job_on_enterprise()

# Location Operation
def select_all_locations():
    local.local_operation.select_all()

def create_local():
    local.local_operation.create_location()

def update_local():
    local.local_operation.update_local()


# Enterprise Operation
def select_all_enterprise():
    return enterprise.enterprise_operation.select_all()

def create_enterprise():
   enterprise.enterprise_operation.create_enterprise()

def update_enterprise():
    enterprise.enterprise_operation.update_enterprise()


def quantidadePeoplesInJobs():
    job.jobs_operation.quantidadePorJob()

