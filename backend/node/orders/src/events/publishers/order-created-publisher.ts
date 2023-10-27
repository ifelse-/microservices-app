import { Publisher, OrderCreatedEvent, Subjects } from '@scriptmotor/common';

export class OrderCreatedPublisher extends Publisher<OrderCreatedEvent> {
  subject: Subjects.OrderCreated = Subjects.OrderCreated;
}
